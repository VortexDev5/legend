import requests

# === CONFIGURATION ===
GITHUB_TOKEN = "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"
REPO_OWNER = "VortexDev5"
REPO_NAME = "legend"

# List of custom issues
issues = [
    {"title": "🐛 Login issue", "body": "Login fails when using mobile browser."},
    {"title": "🎨 UI improvement", "body": "Make the header sticky on scroll."},
    {"title": "🚀 Add dark mode", "body": "Implement toggle for dark mode."},
    {"title": "📦 Update packages", "body": "Upgrade dependencies to latest version."},
    {"title": "📝 Write README", "body": "Add setup and usage instructions."},
    {"title": "🌐 Add i18n support", "body": "Start with French and Spanish translations."},
    {"title": "🔒 Implement 2FA", "body": "Add 2-factor authentication for users."},
    {"title": "📊 Add analytics", "body": "Track page views with Plausible or GA."},
    {"title": "🧪 Write unit tests", "body": "Start with auth module."},
    {"title": "💡 Suggestion form", "body": "Add a simple feedback form on homepage."}
]

# === POST ISSUES ===
url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

for i, issue in enumerate(issues, start=1):
    payload = {
        "title": issue["title"],
        "body": issue["body"],
        "labels": ["auto"]
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        issue_url = response.json()["html_url"]
        print(f"✅ Issue {i} created: {issue_url}")
    else:
        print(f"❌ Failed to create issue {i}: {response.status_code} - {response.text}")
