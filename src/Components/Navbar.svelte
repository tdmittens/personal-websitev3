<script>
    import { Link } from "svelte-routing"
</script>


<main>
    <div class="navbar-container">
        <div class="navbar-logo">
            <h4>Tarandeep Mittal</h4>
        </div>
        <nav class="navbar-links">
            <Link to="/">Home</Link>
            <Link to="music">Music</Link>
            <Link to="projects">Projects</Link>
        </nav>
    </div>
</main>


<style>
    .navbar-container {
        display:flex;
        justify-content: space-around;
        align-items: center;
        height: 10vh;
        background-color: #1c1b22;
    }
    .navbar-logo {
        color: white;
        text-transform: uppercase;
        letter-spacing: 5px;
    }
    .navbar-links {
        display:flex;
        justify-content: space-around;
        width: 30%;
        list-style-type: none;    
        color: white;
        text-decoration: none;
        letter-spacing: 3px;
        font-weight: bold;
        font-size: 14px;    
    }
</style>