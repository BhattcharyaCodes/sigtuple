import { browser, protractor ,  element, by} from "protractor";

describe('Swapi', () =>{

    let url = "https://www.bookmyshow.com/";
    let bmshowLogo = element(by.css(a[title="BookMyShow"]));


    beforeEach(async () => {
        await browser.get(url);
        await browser.actions().sendKeys(protractor.Key.ESCAPE).perform();
        // webdriver equivqlent of //driver.switchTo().alert().dismiss();
        //driver.switchTo().alert().accept();


    });

    it('should find the underlying element present on the screen after the alert is dismissed', async () => {
        expect(await browser.getCurrentUrl()).toEqual(url);
        //check wether the bookmyshow logo is present or not
        expect(bmshowLogo).toBePresent();

       });
});