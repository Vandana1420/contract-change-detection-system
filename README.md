📄 Contract Change Analyzer

A lightweight web application that compares two versions of a contract and highlights differences in a structured and visually intuitive way. Built using Streamlit and Python, this tool helps users quickly identify added, removed, and modified content.

## Features
📂 Upload two contract files (.txt)

🔍 Line-by-line comparison

🟥 Highlights removed/changed lines (Old Contract)

🟩 Highlights added/updated lines (New Contract)

⚖️ Handles unequal file lengths (extra lines detection)

🎯 Clean side-by-side comparison UI

## How It Works
Files are uploaded and read as text

Text is split into lines for structured comparison

Matching lines are compared using Python logic

Differences are highlighted:

  Red → Removed/changed content
  Green → Added/updated content
  
Extra lines are handled separately to maintain alignment
