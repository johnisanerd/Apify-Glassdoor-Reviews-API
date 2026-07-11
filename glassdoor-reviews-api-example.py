"""
Glassdoor Reviews API: A Quick Start Example
See more at: https://apify.com/johnvc/glassdoor-reviews-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/glassdoor-reviews-api/input-schema?fpr=9n7kx3

This script shows how to call the Glassdoor Reviews API on Apify from Python and
read its structured JSON output. Give it one or more Glassdoor company review URLs
and it returns one clean row per review: overall and per-category ratings,
employment type and status, review dates, and review URLs.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Kept small on purpose: one company URL, maxReviewsPerCompany set to 5, and a
# short 30-day window, so your first run stays cheap (you pay per review returned).
# Raise maxReviewsPerCompany, widen days, or add more company URLs to collect more.
run_input = {
    "companyUrls": ["https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm"],
    "maxReviewsPerCompany": 5,
    "days": 30,
    # Add more companies to batch them in one run:
    # "companyUrls": [
    #     "https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm",
    #     "https://www.glassdoor.com/Reviews/Microsoft-Reviews-E1651.htm",
    # ],
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/glassdoor-reviews-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} review(s).\n")

# Show a few key fields from each review.
for item in items:
    print(f"Company:    {item.get('companyName')}")
    print(f"Overall:    {item.get('overallRating')}")
    print(f"Employee:   {item.get('employmentType')} ({item.get('employmentStatus')})")
    print(f"Published:  {item.get('datePublished')}")
    print(f"Pros:       {item.get('pros')}")
    print(f"Cons:       {item.get('cons')}")
    print(f"URL:        {item.get('reviewUrl')}")
    print(f"Summary:    {item.get('summary')}")
    print("-" * 60)

# The Ratings Breakdown fields (per-category scores) are on every review row too:
#   ratingCareerOpportunities, ratingCompensationBenefits, ratingCultureValues,
#   ratingWorkLife, ratingSeniorLeadership, ratingDiversityInclusion
# Sub-ratings a reviewer did not rate are omitted rather than returned as zero.
