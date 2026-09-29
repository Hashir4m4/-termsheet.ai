const { chromium } = require('playwright');

(async () => {
    console.log("Starting Browser E2E Test...");
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    
    try {
        page.on('console', msg => console.log('BROWSER CONSOLE:', msg.text()));
        page.on('pageerror', error => console.log('BROWSER ERROR:', error.message));
        console.log("Navigating to dashboard...");
        await page.goto('http://127.0.0.1:8000/static/index.html', { waitUntil: 'networkidle' });
        
        console.log("Page title:", await page.title());
        
        // Select CloudForge and load intelligence
        await page.selectOption('#vendorSelect', 'CloudForge');
        await page.click('button:has-text("Load Intelligence")');
        
        // Wait for profile to load (increase timeout to handle LLM delays)
        await page.waitForSelector('#profile:visible', { timeout: 60000 });
        const vName = await page.innerText('#vName');
        console.log("Loaded profile for:", vName);
        
        const obs = await page.innerText('#observations');
        if (obs && obs.length > 5) {
            console.log("Hindsight Observation loaded successfully.");
        } else {
            throw new Error("Observation text not found.");
        }
        
        // Generate strategy
        await page.fill('#offer', '$120k');
        await page.click('button:has-text("Get Strategy")');
        
        await page.waitForSelector('#strategyResult h3', { timeout: 60000 });
        const strategy = await page.innerText('#strategyResult');
        if (strategy.includes("Memory")) {
            console.log("Hindsight Strategy generated successfully.");
        } else {
            throw new Error("Strategy text not correct.");
        }
        
        console.log("BROWSER E2E TEST PASSED.");
    } catch (error) {
        console.error("E2E TEST FAILED:", error.message);
        process.exit(1);
    } finally {
        await browser.close();
    }
})();
