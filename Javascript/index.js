const {Builder, By,Key,util} =require("selenium-webdriver");
let driver =  new Builder().forBrowser("firefox").build();
const delay = ms => new Promise(res => setTimeout(res, ms));
async function openwebsites()
{
    try
    {
        await driver.get('https://sakshingp.github.io/assignment/login.html')
        console.log("username & password genrating")
        await delay(2000);
        await driver.findElement(By.id("username")).sendKeys(generateusername());
        await driver.findElement(By.id("password")).sendKeys(generateusername());
        await delay(500);
        await driver.findElement(By.id("log-in")).click();
        console.log("login successful");
        await delay(2000);
        console.log("Sorting elements.........");
        try
        {
            var actual = await driver.findElements(By.xpath("//tbody/tr[1]/td[5]/span"))
            var actualList=[]
            var tempList =[]
            var sortList=[]
            for (var i=0;i< actual.length;i++){
                 actualList.push(actual[i].getText())
                tempList.push(actual[i].getText())
                }
            tempList=actual;
            sortList=actualList.sort;
            var tempFlag= true
            for (var i=0;i< actual.length;i++){
                if(actualList[i]==sortList[i]){
                 }
             else{
                tempFlag= false
                 break;
                }
            }
            if(tempFlag= true){
            console.log("amount is sorted order")
            await driver.findElement(By.id("amount")).click();
            }
            else{
                console.log("amount is not sorted order")
           }
        }
        catch(error)
        {
            console.log(error);
        } 
    }
    catch(error)
    {
        console.log(error);
    }
}
openwebsites();
function generateusername()
{
    var arr = "ABCDEFGHIJKLMNOPQRSTUVWXTZabcdefghiklmnopqrstuvwxyz1234567890";  
    var len = 7;  
    var randomstring = '';
    for (var i=0; i<len; i++) {  
        var rnum = Math.floor(Math.random() * arr.length);  
        randomstring +=arr.substring(rnum, rnum+1);  
    }     
    return randomstring
}

