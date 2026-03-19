# Quantum Machine Learning Applications: Systematic Literature Mapping

This repository contains the dataset and processing scripts for a Rapid Review investigating applied Quantum Machine Learning (QML). The project systematically maps real-world application domains to specific QML models based on scientific literature published between 2023 and 2026.

## Contents

*   **`scopus_results/`**: Raw and filtered bibliographic data retrieved from the Scopus database.
*   **`slm_processing.ipynb`**: The primary analytical pipeline. It implements an automated, LLM-assisted data extraction process using the Google Gemini API to identify application domains and QML architectures from abstracts. It also includes the code for validating the LLM output against a manually extracted pilot set.
*   **`results/`**: The final synthesized outputs, which include:
    *   `extracted_keywords.csv`: The complete dataset of mapped domains and models.
    *   `cross_table.xlsx`: A cross-tabulation matrix correlating the top 5 application domains with the most frequently utilized QML models.
    *   `vosviewer_map.txt` & `vosviewer_network.txt`: Bipartite network data formatted for VOSviewer to visualize the co-occurrence of QML domains and models.
