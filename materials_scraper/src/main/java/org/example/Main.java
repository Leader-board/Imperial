package org.example;

import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

import java.io.File;

public class Main {
    public static void scraper(String username, String password, List<String> modules) throws InterruptedException {
        String userdirectory = new File("").getAbsolutePath();
       // System.setProperty("webdriver.chrome.driver", "C:\\chromedriver.exe");
       System.out.println(userdirectory);
        System.setProperty("webdriver.chrome.driver", userdirectory + "/chromedriver");
        String downloadFilepath = "/vol/bitbucket/dm1321/materials";
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--headless");
        HashMap<String, Object> chromePrefs = new HashMap<String, Object>();
        chromePrefs.put("download.default_directory", downloadFilepath);
        options.setExperimentalOption("prefs", chromePrefs);
        WebDriver driver = new ChromeDriver(options);
        // will ask for login
        driver.get("https://materials.doc.ic.ac.uk/");
        WebElement wb = driver.findElement(By.xpath("//*[@id=\"username\"]"));
        wb.sendKeys(username);
        wb = driver.findElement(By.xpath("//*[@id=\"password\"]"));
        wb.sendKeys(password);
        wb.sendKeys(Keys.ENTER);
        // now we can iterate as required
        for (String m:modules)
        {
            String togo = "https://materials.doc.ic.ac.uk/download/2122/" + m + "?";
            System.out.println(togo);
            driver.get(togo);
        }
    }
    public static void main(String[] args) throws InterruptedException {
        scraper(args[0], args[1], Arrays.asList("40001","40004R","40005","40006R","40007","40008","40009","40012","40016","40017","40018","40018A","50001","50002","50003","50004","50005","50006","50007.1","50007.2","50007.3","50008","50009","50010","50010.2","50011","60001","60002","60003","60005","60006","60007","60008","60009","60010","60012","60013","60015","60016","60017","60019","60020","60021","60023","60024","60025","60026","70001","70004","70005","70006","70007","70008","70009","70010","70011","70012","70015","70016","70017","70018","70019","70020","70022","70023","70024","70025","70026","70027","70028","70030","70031","70032","70033","70034","70035","70036","70037","70039","70040","70041","70042","70043","70044","70045","70046","70047","70048","70049","70050","70051","70052","70053","70055","70056","70057","70058","70059","70060","70061","70066","70067","70068","70069","70152","70153","70154"));
      //  System.out.println("Hello world!");
    }
}