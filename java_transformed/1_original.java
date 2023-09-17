public class DummyClass {
	private Collection<ApplicationContextInitializer<?>> getInitializers() {
		List<ApplicationContextInitializer<?>> initializers = new ArrayList<>();
		initializers.add(new RestartScopeInitializer());
		return initializers;
	}
}