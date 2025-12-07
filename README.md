### Marp Presentation Code

````markdown
---
marp: true
theme: gaia
paginate: true
backgroundColor: #ffffff
author: "Technical Writing Team"
math: mathjax
style: |
  /* Custom Theme Specification */
  section {
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 30px;
    padding: 70px;
  }
  /* Brand Colors */
  h1 {
    color: #2563eb; /* Royal Blue */
    font-size: 60px;
  }
  h2 {
    color: #1e40af;
    border-bottom: 2px solid #cbd5e1;
  }
  /* Code Block Styling */
  code {
    background: #f1f5f9;
    color: #d946ef;
  }
  /* Custom Footer placement */
  footer {
    position: absolute;
    bottom: 20px;
    left: 70px;
    font-size: 18px;
    color: #64748b;
  }
---

# Product Documentation Strategy
## Moving to Docs-as-Code

**Prepared by:** Technical Writing Lead
**Contact:** 22f1001255@ds.study.iitm.ac.in

---

# Why Marp?

As technical writers, we need tools that fit our existing engineering workflows.

* **Version Control:** Text-based files (`.md`) are easily diffable in Git.
* **Maintainability:** Content separates from design.
* **Portability:** Export to HTML, PDF, or PPTX from a single source.
* **CI/CD Friendly:** Can be built automatically via GitHub Actions.

---

# Backend Optimization Logic

We are updating the sorting algorithm for the user dashboard. The complexity has been reduced significantly.

**Previous Complexity:** $O(n^2)$
**Current Complexity:** $O(n \log n)$

The core efficiency is defined by the following summation:

$$
T(n) = \sum_{i=1}^{\log n} 2^i \cdot \frac{n}{2^i} = n \log n
$$

---

![bg right:40%](https://images.unsplash.com/photo-1555066931-4365d14bab8c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1000&q=80)

# Infrastructure Overview

This slide utilizes the **split background** directive.

* **Left Side:** Content and bullet points.
* **Right Side:** Visual representation of our coding environment.

This layout is ideal for showcasing code snippets alongside their visual output or architectural diagrams.

---

# Custom Directives & Code

We use scoped directives to change specific slides without affecting the global theme.

```javascript
// Example of the API endpoint we are documenting
const getProductData = async (id) => {
  try {
    const response = await api.get(`/products/${id}`);
    return response.data;
  } catch (error) {
    console.error("Documentation needed for error: ", error);
  }
};
````

> "Good documentation is like a love letter that you write to your future self."

-----

# Thank You

**Questions?**

Email: 22f1001255@ds.study.iitm.ac.in
GitHub: @technical-writer-team

```
