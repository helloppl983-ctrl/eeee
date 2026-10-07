import asyncio
from playwright.async_api import async_playwright
import getpass

async def automate_gmail_login():
    async with async_playwright() as p:
        # Launch Chrome browser
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        # Navigate to Gmail login
        await page.goto("https://accounts.google.com/signin")

        # Wait for email input to be visible
        await page.wait_for_selector('input[type="email"]')

        # Fill email field
        email = "connorpage98@gmail.com"
        await page.fill('input[type="email"]', email)
        print(f"✓ Email filled: {email}")

        # Press Enter/Next to go to password field
        await page.press('input[type="email"]', "Enter")

        # Wait for password field to appear
        await page.wait_for_selector('input[type="password"]', timeout=5000)

        # Prompt user for password (secure input)
        password = getpass.getpass("Enter your Gmail password: ")

        # Fill password field
        await page.fill('input[type="password"]', password)
        print("✓ Password filled")

        # Press Enter to login
        await page.press('input[type="password"]', "Enter")

        # Wait for login to complete
        print("⏳ Logging in... Please wait")
        await page.wait_for_url("https://mail.google.com/*", timeout=10000)

        print("✓ Login successful!")
        print("Browser will stay open. Close it when done.")

        # Keep browser open
        await asyncio.sleep(300)  # Stay open for 5 minutes
        await browser.close()

if __name__ == "__main__":
    asyncio.run(automate_gmail_login())
