from playwright.async_api import async_playwright

from config.configuration import URL

async def toggle_media_state(remove_if_off: bool):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(URL)

        is_music_on = await page.evaluate('''() => {
            const media = document.querySelector('video[name="media"]');
            return !!(media && !media.paused);
        }''')

        if not is_music_on and remove_if_off:
            await page.evaluate('''() => {
                const media = document.querySelector('video[name="media"]');
                if (media) {
                    media.pause();
                    media.remove();  // Удаляем элемент video
                }
            }''')

        await page.wait_for_timeout(5000)

        await browser.close()