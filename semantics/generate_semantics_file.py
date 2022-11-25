# pip install pandas 
import pandas as pd
from markdownTable import markdownTable

# Read the csv file
semantic_classes = {
    "Full Lexicon": pd.read_csv("full_lexicon.csv", delimiter=";"),
    "Binary Operators": pd.read_csv("binary_operators.csv", delimiter=";"),
    "Comparions Operators": pd.read_csv("comparison_operators.csv", delimiter=";"),
    "Instanciation": pd.read_csv("instanciation.csv", delimiter=";"),
    "Truth Values": pd.read_csv("truth_values.csv", delimiter=";"),
    "Parenthesis": pd.read_csv("parenthesis.csv", delimiter=";"),
    "Functions": pd.read_csv("functions.csv", delimiter=";"),
    "If Else Statements": pd.read_csv("if_else_statements.csv", delimiter=";"),
    "While Loops": pd.read_csv("while.csv", delimiter=";"),
    "Lists": pd.read_csv("lists.csv", delimiter=";"),
    "Dictionaries": pd.read_csv("dicts.csv", delimiter=";"),
}


semantics_file = open("../semantics.md", "w")

semantics_file.write("# Table of Contents\n")
for (class_name, class_df) in semantic_classes.items():
    semantics_file.write(f"1. [{class_name.replace(' ', '-')}](#{class_name.replace(' ', '-')})\n")

for (class_name, class_df) in semantic_classes.items():
    semantics_file.write(f"## <a name='{class_name}'>{class_name}</a>\n")
    semantics_file.write(markdownTable(class_df.to_dict(orient='records')).setParams(row_sep = 'markdown', padding_width = 10, quote = False).getMarkdown())
    semantics_file.write("\n")
