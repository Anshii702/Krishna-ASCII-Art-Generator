# 🪶 Lord Krishna Colored ASCII Art Generator

A Python-based image processing tool that converts high-contrast images into detailed, high-resolution, and color-mapped ASCII art rendered as custom HTML output.

---

## 🎨 Overview

This project takes an input image (such as the divine silhouette of Lord Krishna) and processes pixel brightness and RGB color values using Python's `Pillow` library. Instead of rendering standard monochrome terminal output, it generates a styled HTML file preserving exact source colors, contrast, and sharp detail.

---

## ✨ Features

* **Image Preprocessing:** Uses `Pillow` (PIL) to enhance image contrast and sharpness for crisp detail.
* **RGB Color Mapping:** Maps pixel RGB values directly to dynamic HTML `<span>` tags.
* **Custom Character Density:** Maps grayscale brightness levels to a granular 70-character ASCII density scale.
* **Browser-Ready Output:** Generates `krishna_colored_art.html` for clean, responsive viewing across devices.

---

## 📁 Repository Structure

```text
Krishna-ASCII-Art-Generator/
│
├── app.py                      # Main Python script for ASCII conversion
├── krishna.jpg                 # Input image
└── krishna_colored_art.html    # Generated colored ASCII art output
