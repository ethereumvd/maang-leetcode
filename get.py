import subprocess
import shutil
import os

companies = [
    "Google",
    "Meta",
    "Amazon",
    "Apple",
    "Flipkart",
    "Netflix",
    "Barclays",
    "Atlassian",
    "DE Shaw",
    "Goldman Sachs",
    "JP Morgan",
    "Morgan Stanley",
    "Jane Street",
    "Jump Trading"
]

repo_url = "https://github.com/liquidslr/leetcode-company-wise-problems.git"
clone_dir = "full_repo"
output_dir = "selected_companies"

print("cloning full repo...")
subprocess.run(["git", "clone", repo_url, clone_dir])

os.makedirs(output_dir, exist_ok=True)

for company in companies:
    src = os.path.join(clone_dir, company)
    dst = os.path.join(output_dir, company)
    if os.path.exists(src):
        print(f"copying {company}...")
        shutil.copytree(src, dst)
    else:
        print(f"folder '{company}' not found in repo")

shutil.rmtree(clone_dir)
print("cleaned full repo")
