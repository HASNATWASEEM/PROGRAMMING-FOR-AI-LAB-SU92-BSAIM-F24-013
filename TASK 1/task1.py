from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import re
import csv
import os

web_app = Flask(__name__)

DATA_FILE = "collected_emails.csv"

# Function to extract emails
def extract_email_list(site_link):
    try:
        page_data = requests.get(site_link, timeout=10)
        parsed_html = BeautifulSoup(page_data.text, "html.parser")
        visible_text = parsed_html.get_text()

        email_collection = set(re.findall(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            visible_text
        ))

        return email_collection

    except Exception as error_msg:
        print("Scraping Error:", error_msg)
        return set()


# Function to store emails in CSV
def store_emails_csv(site_link, email_collection):

    file_available = os.path.isfile(DATA_FILE)

    with open(DATA_FILE, "a", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)

        if not file_available:
            csv_writer.writerow(["Website", "Email_Address"])

        for single_email in email_collection:
            csv_writer.writerow([site_link, single_email])


# Home route
@web_app.route("/", methods=["GET", "POST"])
def homepage():

    found_emails = []
    website_input = ""

    if request.method == "POST":

        website_input = request.form.get("url")

        if website_input:
            found_emails = extract_email_list(website_input)

            if found_emails:
                store_emails_csv(website_input, found_emails)

    return render_template("index.html", emails=found_emails, url=website_input)


if __name__ == "__main__":
    web_app.run(debug=True, use_reloader=False)