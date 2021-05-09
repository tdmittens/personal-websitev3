<script>
	import { Router, Link, Route } from "svelte-routing"

	import Home from './Components/Home.svelte'
	import About from './Components/About.svelte'
	import Music from './Components/Music.svelte'
	import Projects from './Components/Projects.svelte'

	export let url = "" ;

</script>

<Router url="{url}">
	<div>
		<Route path="projects" component="{Projects}" />
		<Route path="music" component="{Music}" />
		<Route path="about"><About /></Route>
		<Route path="resume"></Route>
		<Route path="/"><Home /></Route>
	</div>
</Router>