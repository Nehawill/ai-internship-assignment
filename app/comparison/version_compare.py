def compare_versions(v1_sections, v2_sections):
    """
    Compare two document versions and return
    Added, Removed, Modified and Unchanged sections.
    """

    results = []

    # Create lookup dictionaries using section title
    v1_dict = {section.title: section for section in v1_sections}
    v2_dict = {section.title: section for section in v2_sections}

    # Get every unique title
    all_titles = set(v1_dict.keys()) | set(v2_dict.keys())

    for title in sorted(all_titles):

        if title not in v1_dict:
            status = "Added"

        elif title not in v2_dict:
            status = "Removed"

        elif v1_dict[title].content == v2_dict[title].content:
            status = "Unchanged"

        else:
            status = "Modified"

        results.append({
            "title": title,
            "status": status,
            "old_content": v1_dict[title].content if title in v1_dict else None,
            "new_content": v2_dict[title].content if title in v2_dict else None
        })

    return results