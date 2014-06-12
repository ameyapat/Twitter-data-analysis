package auth;

import twitter4j.conf.Configuration;
import twitter4j.conf.ConfigurationBuilder;

public class ConfigBuilder {
	private static Configuration config;
	
	private static final String API_KEY = "yTTOL3w9mRglTNSyLpiRw";
	private static final String API_SECRET = "VWu6dehIAJK6lG9gZKyImDPuYTM74Qto1yNSEdbnN8";
	private static final String ACCESS_TOKEN = "43357436-FXpuUfgucxU988uuDaCGbQGnlBF7HU1CKL4mVwyZ2";
	private static final String ACCESS_SECRET = "dguq1eV7CIjhD70COF9sBRdv4PLPz5SS5JhI3IycWbUPx";
	
	static {
		ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true);
		cb.setOAuthConsumerKey(API_KEY);
		cb.setOAuthConsumerSecret(API_SECRET);
		cb.setOAuthAccessToken(ACCESS_TOKEN);
		cb.setOAuthAccessTokenSecret(ACCESS_SECRET);
		config = cb.build();
	}
	
	public static Configuration getConfig() {
		return config;
	}
}
