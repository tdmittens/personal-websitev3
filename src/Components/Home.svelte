<script>
import Navbar from './Navbar.svelte'
let src_image = "me.jpeg"

</script>

<main>
    <Navbar/>
    <div class="bio">
        <div class="bio-picture">
            <img class="bio-picture-specs" src={src_image} alt="Tarandeep Mittal">
        </div>
        <div class="bio-text">
            <p>
                Hi, I'm Tarandeep! Currently, I'm based in Toronto and have recently finished my Industrial Engineering degree at Ryerson University.
                In my free time, I find myself playing <a href="https://steamcommunity.com/id/dipmaestro/"> video games</a>, 
                solving variants of the <a href="https://www.worldcubeassociation.org/persons/2014MITT02">rubik's cube</a>, 
                and listening to lots of <a href="https://open.spotify.com/user/mittaltarandeep">music</a>!
            </p>
            <p>
                Feel free to download my <a target="_blank" rel="noreferrer" href="/resume">resume</a>, 
                look at  <a target="_blank" rel="noreferrer" href="https://github.com/tdmittens">my GitHub</a>, or
                send me an <a href="mailto:tarandeepmittal@gmail.com">email!</a> I'm always happy to meet new people!
            </p>
        </div>
        <div class="bio-gitactivity">
            <img class="bio-github" src="https://ghchart.rshah.org/tdmittens" alt="tdmittens's Github chart">
        </div>
        
        <div class="bio-footer">
            <p>Designed and <a href="https://github.com/tdmittens/personal-websitev3"> developed </a> with ❤ and 😭.</p>            
        </div>
    </div>
</main>

<style>
    p {
        text-align: left;
    }
    .bio {
        padding-top: 20px;
        padding-right: 30vw;
        padding-bottom: 20px;
        padding-left: 30vw;
        display:flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
    }
    .bio-picture{
        flex: 1 0 30%;
    }
    .bio-text{
        flex: 1 1 40%;
    }
    .bio-gitactivity{
        flex: 1 1 20%;
    }
    .bio-footer{
        flex: 1 1 10%;
        
    }
    .bio-picture-specs{
        filter: grayscale(40%);
        max-height: 40vh;
        max-width: 100%;
        border-radius: 40px;
        left: 0;
        top: 0;
    }
    .bio-github {
        filter: invert(97%) hue-rotate(195deg) grayscale(0.4);
        max-width: 100%; 
    }
</style>