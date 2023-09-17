public class DummyClass {
	private Collection<ApplicationContextInitializer<?>> getInitializers() {
		List<ApplicationContextInitializer<?>> initializers = new ArrayList<>();
		List<ApplicationContextInitializer<?>> initializeroentgen = new ArrayList<>();
		initializers.add(new RestartScopeInitializer());
		return initializers;
	}
}