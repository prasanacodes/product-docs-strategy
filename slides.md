### Marp Presentation Code

````markdown
---
marp: true
theme: default
paginate: true
backgroundColor: #f8f9fa
author: "Technical Writing Team"
math: mathjax
style: |
  /* Custom Theme Specification */
  section {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    padding: 60px;
    font-size: 28px;
  }
  h1 {
    color: #0d6efd;
    font-size: 60px;
  }
  h2 {
    color: #495057;
    border-bottom: 3px solid #dee2e6;
  }
  code {
    background-color: #e9ecef;
    color: #d63384;
    padding: 0.2em 0.4em;
    border-radius: 4px;
  }
---

# Product Documentation Strategy
## Q4 Engineering Roadmap

**Presenter:** Tech Writing Lead
**Email:** 22f1001255@ds.study.iitm.ac.in

---

# Overview of Directives

This presentation uses specific **Marp Directives** to alter layouts on a per-slide basis.

* **Global Directives:** Defined in the YAML header (e.g., `paginate: true`).
* **Local Directives:** Defined in HTML comments (like the footer below).

> Directives allows us to maintain a clean source file while producing rich visual output.

---

# Algorithmic Complexity

We adhere to strict performance standards. The documentation must reflect the algorithmic efficiency of our parser.

**Efficiency Formula:**

$$
T(n) = \sum_{k=0}^{n-1} (3k^2 + 2k) = O(n^3)
$$

The complexity $O(n^3)$ indicates that optimization is required for large datasets.

---

# Dark Mode Slide

This slide uses the `_backgroundColor` and `_color` **directives** locally to inverse the colors just for this specific page.

* Useful for code deep-dives.
* Reduces eye strain during long presentations.

```python
def generate_docs():
    print("Building documentation...")
    return True
````

-----

# Visual Layouts

This slide uses the **Background Image directive** (`bg right:40%`) to split the slide.

1.  **Text:** Remains on the left.
2.  **Image:** Automatically fills the right 40%.
3.  **Responsiveness:** Marp handles the scaling.

Perfect for showing product screenshots alongside descriptive text.

-----

# Thank You

**Contact Information**
22f1001255@ds.study.iitm.ac.in

*Documentation Source hosted on GitHub*

```

### Directives Used in This File

1.  **``**: Used on the title slide to invert the colors (dark background, light text) specifically for that slide.
2.  **``**: Used on the title slide to hide the page number (slide 1).
3.  **``**: Added on the second slide to apply a footer to that slide and all subsequent slides.
4.  **``**: Used to manually override the background color for the "Dark Mode Slide".
5.  **`![bg right:40%](...)`**: A specialized image directive that sets the image as a background and splits the layout.
```
