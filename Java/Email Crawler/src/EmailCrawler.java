import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.ArrayList;
import java.net.URL;


public class EmailCrawler {
	public static void main(String[] args) throws IOException
	{
		String givenURL = "http://www.weather.com";
		String authority;
		
		{
			URL mainURL = new URL(givenURL);
			authority = mainURL.getAuthority();
		}
		
		String regex = "[a-zA-Z0-9\\.\\-\\_]+@[a-zA-Z]+[\\.]{1}[a-zA-Z]{2,4}";
		Pattern pattern = Pattern.compile(regex);
		
		ArrayList<String> listOfURL = new ArrayList<String>();
		ArrayList<String> listOfEmail = new ArrayList<String>();
		listOfURL.add(givenURL);
		
		//main loop
		for(int i = 0; i < listOfURL.size(); i++)
		{
			givenURL = listOfURL.get(i);
			System.out.print("Connect to " + givenURL + " ");
			
			Document doc = Jsoup.connect(givenURL).get();
			
			//Searches for email and saves the location
			String siteText = doc.text();
			Matcher matcher = pattern.matcher(siteText);
			while(matcher.find())
			{
				if(!listOfEmail.contains(matcher.group()))
					listOfEmail.add(matcher.group());
			}
			
			//Searches and saves URLs without dupes
			Elements scrapedURLS = doc.select("a[href]");
			for(Element tag_a : scrapedURLS)
			{
				String str = tag_a.attr("abs:href");
				URL url = new URL(str);
				if(authority.equals(url.getAuthority()))
				{
					if(!listOfURL.contains(str))
						listOfURL.add(str);
				}
			}
			System.out.print("--- Found Links (" + scrapedURLS.size() +") ");
			System.out.println("Saved links (" + listOfURL.size() + ") ");
		}
		System.out.println("Total links : " + listOfURL.size());
		System.out.println("Total Email Address : " + listOfEmail.size());
	}

}
