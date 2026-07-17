TEST_CASE_PROMPT = """
You are a software QA engineer.

Generate software test cases from the document section below.

Return ONLY valid JSON in this exact format:

{
  "test_cases": [
    {
      "title": "...",
      "steps": [
        "...",
        "..."
      ],
      "expected_result": "..."
    }
  ]
}

Document Section:

{content}
"""