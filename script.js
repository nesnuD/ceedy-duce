let nflint = document.getElementById('nfl-int-btn')
let nflsck = document.getElementById('nfl-sck-btn')
let nfltck = document.getElementById('nfl-tck-btn')
let nflast = document.getElementById('nfl-ast-btn')
let nflfumb = document.getElementById('nfl-fumb-btn')

let nflintvid = document.getElementById('nfl-int-vid')
let nflsckvid = document.getElementById('nfl-sck-vid')
let nfltckvid = document.getElementById('nfl-tck-vid')
let nflastvid = document.getElementById('nfl-ast-vid')
let nflfumbvid = document.getElementById('nfl-fumb-vid')

nflint.onclick = function() {
  nflintvid.style.display = 'block';
  nflintvid.play();
  nfltckvid.style.display = 'none';
  nflsckvid.style.display = 'none';
  nflfumbvid.style.display = 'none';
  nflastvidstyle.display = 'none';
}

nfltck.onclick = function() {
    document.getElementById('nfl-tck-vid').style.display = 'block';
    nfltckvid.play();
    document.getElementById('nfl-int-vid').style.display = 'none';
    document.getElementById('nfl-sck-vid').style.display = 'none';
    document.getElementById('nfl-ast-vid').style.display = 'none';
    document.getElementById('nfl-fumb-vid').style.display = 'none';
}


nflintvid.onended = function () {
    nflintvid.style.display = "none";
}

nfltckvid.onended = function () {
    nfltckvid.style.display = 'none';
}