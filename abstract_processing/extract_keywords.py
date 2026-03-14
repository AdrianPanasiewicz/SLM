import pandas as pd
import time
from pydantic import BaseModel
from google import genai
from google.genai import types
from tqdm import tqdm


class ExtractionResult(BaseModel):
	domains: list[str]
	models: list[str]


client = genai.Client()

df = pd.read_csv("scopus_results/included_results.csv")
abstracts = df[['abstract', 'id']].head(5).to_dict('records')

results = []
rpm_limit = 15

for i, row in enumerate(tqdm(abstracts, desc="Processing abstracts")):
	if i > 0 and i % rpm_limit == 0:
		time.sleep(65)

	prompt = f"""
	You are an expert data extractor for a systematic literature review. Read the following abstract and extract two 
	lists:

	1. 'domains': The specific real-world application domains where the model is being applied (e.g., 'Finance', 
	'Healthcare', 'Telecommunications', 'Chemistry'). Do NOT include machine learning tasks like 'Classification' or 
	'Regression' as domains. If no real-world domain is mentioned, output ['Not Specified'].
	2. 'models': The specific Quantum Machine Learning models or architectures mentioned (e.g., 'Quantum Neural 
	Network', 'Quantum Support Vector Machine', 'Parameterized Quantum Circuit'). Ignore classical models. If none are 
	specified, output ['Not Specified'].

	Abstract:
	{row['abstract']}
	"""

	try:
		response = client.models.generate_content(
			model="gemini-3.1-flash-lite-preview",
			contents=prompt,
			config=types.GenerateContentConfig(
				response_mime_type="application/json",
				response_schema=ExtractionResult,
				temperature=0.0
			)
		)
		results.append({
			"original_index": i,
			"doi": row['id'],
			"extracted_data": response.text
		})
	except Exception as e:
		results.append({
			"original_index": i,
			"doi": row['id'],
			"extracted_data": {"error": str(e)}
		})

output_df = pd.DataFrame(results)
output_df.to_csv(r"results\extracted_keywords.csv", index=False)
