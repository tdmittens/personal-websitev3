<script>
    import Navbar from "./Navbar.svelte";
    
</script>

<main>
    <Navbar/>
    <h1>Still updating!</h1>
    <div class="music-container">
        <div class="music-section">
            <h2>Top 10 Songs</h2>
            <iframe src="https://open.spotify.com/embed/playlist/2KQsKqJPdzB5dd13yOD0dE" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media" title="Top 10 Songs"></iframe>
        </div>
        <div class="music-section">
            <h2>Korean Rotation</h2>
            <iframe src="https://open.spotify.com/embed/playlist/1GoyVE3X1hOiLIQTQYKgsw" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media" title="Korean Rotation"></iframe>
        </div>
        <div class="music-section">
            <h2>English Rotation</h2>
            <iframe src="https://open.spotify.com/embed/playlist/4nHTuByk8YV1H2sRkOnatd" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media" title="English Rotation"></iframe>
        </div>
        <div class="music-section">
            <h2>Favourite Mix</h2>
            <iframe src="https://open.spotify.com/embed/playlist/3EwVOzbLnNGsiPeb4NyDyI" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media" title="Current Favourite Mix"></iframe>
        </div>
    </div>
</main>


<style>
    .music-container{
        padding-top:5vh;
        display:flex;
        flex-direction:row;
        flex-wrap: wrap;
        align-content: center;
        align-items: center;
        width: 100vw;
    }
    .music-section{
        flex: 1 1 auto;
        text-align: center;
    }
</style>