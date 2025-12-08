---

````markdown
---
marp: true
title: Product Documentation Overview
author: 22f1001255@ds.study.iitm.ac.in
theme: default
paginate: true
---

<style>
/* Custom theme overrides */
section {
  background-color: #f8fafc;
  color: #1f2937;
  font-family: "Segoe UI", sans-serif;
}
h1, h2 {
  color: #2563eb;
}
code {
  background-color: #e5e7eb;
}
</style>

<!-- _class: lead -->
# Product Documentation
### Maintainable • Versioned • Portable

Author: 22f1001255@ds.study.iitm.ac.in

---

<!-- _header: Product Docs -->
<!-- _footer: Version-controlled with Git -->

## Why Marp for Documentation?

- Markdown-based workflow
- Easy Git diff & collaboration
- Single source → HTML / PDF / PPTX
- Developer-friendly tooling

---

## Architecture Overview

![bg cover](docs-bg.png)

### Documentation Pipeline

1. Write Markdown
2. Style with CSS
3. Export to required formats
4. Publish or share

---

<!-- _backgroundColor: #0f172a -->
<!-- _color: #e5e7eb -->

## Custom Styling with Directives

This slide uses:
- Custom background color
- Custom text color
- CSS-based theme extensions

Great for **highlight slides** in product docs.

---

## Algorithmic Complexity Example

We often describe performance characteristics in docs.

### Time Complexity

Inline math:  
The average lookup time is $O(1)$

Block math:
$$
T(n) = T(n-1) + O(1) \Rightarrow T(n) = O(n)
$$

---

## Code Example

```python
def search(items, target):
    for item in items:
        if item == target:
            return True
    return False
````

* Time Complexity: $O(n)$
* Space Complexity: $O(1)$

---

## Documentation Best Practices

* Keep slides concise
* Use relative asset paths
* Avoid embedding binary data
* Review changes via Git history
* Automate export in CI/CD

---

<!-- _footer: © Software Engineering Team -->

## Thank You

Questions or feedback?
📧 **[22f1001255@ds.study.iitm.ac.in](mailto:22f1001255@ds.study.iitm.ac.in)**

```

---
