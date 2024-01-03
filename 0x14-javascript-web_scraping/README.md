## JavaScript Web Scraping

## Tasks:
### [0-readme.js](./0-readme.js)
Write a script that reads and prints the content of a file.

```
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# cat cisfun 
C is super fun!
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# ./0-readme.js cisfun 
C is super fun!

root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# ./0-readme.js doesntexist
[Error: ENOENT: no such file or directory, open 'doesntexist'] {
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist'
}
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping#
```

### [1-writeme.js](./1-writeme.js)
Write a script that writes a string to a file.

```
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# ./1-writeme.js my_file.txt "Python is cool"
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# cat my_file.txt ; echo ""
Python is cool
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping#
```

### [2-statuscode.js](./2-statuscode.js)
Write a script that display the status code of a GET request.

```
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping#
```

### [3-starwars_title.js](./3-starwars_title.js)
Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

```
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# ./3-starwars_title.js 1
A New Hope
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# ./3-starwars_title.js 5
Attack of the Clones
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping#
```

### [4-starwars_count.js](./4-starwars_count.js)
Write a script that prints the number of movies where the character “Wedge Antilles” is present.

```
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# 
```

### [5-request_store.js](./5-request_store.js)
Write a script that gets the contents of a webpage and stores it in a file.

```
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# ./5-request_store.js http://loripsum.net/api loripsum
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nihil opus est exemplis hoc facere longius. Duo Reges: constructio interrete. </p>

<p>Ut optime, secundum naturam affectum esse possit. Ipse Epicurus fortasse redderet, ut Sextus Peducaeus, Sex. Ex rebus enim timiditas, non ex vocabulis nascitur. Quo plebiscito decreta a senatu est consuli quaestio Cn. Cum autem venissemus in Academiae non sine causa nobilitata spatia, solitudo erat ea, quam volueramus. Sin te auctoritas commovebat, nobisne omnibus et Platoni ipsi nescio quem illum anteponebas? Quid turpius quam sapientis vitam ex insipientium sermone pendere? Idem iste, inquam, de voluptate quid sentit? Sed haec quidem liberius ab eo dicuntur et saepius. Quis enim potest ea, quae probabilia videantur ei, non probare? Quamquam id quidem, infinitum est in hac urbe; Nonne igitur tibi videntur, inquit, mala? Graecum enim hunc versum nostis omnes-: Suavis laborum est praeteritorum memoria. </p>

<p>Apud imperitos tum illa dicta sunt, aliquid etiam coronae datum; Quid igitur dubitamus in tota eius natura quaerere quid sit effectum? Non dolere, inquam, istud quam vim habeat postea videro; Cur tantas regiones barbarorum pedibus obiit, tot maria transmisit? Non autem hoc: igitur ne illud quidem. Negat enim summo bono afferre incrementum diem. Piso igitur hoc modo, vir optimus tuique, ut scis, amantissimus. Levatio igitur vitiorum magna fit in iis, qui habent ad virtutem progressionis aliquantum. </p>

root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping#
```

### [6-completed_tasks.js](./6-completed_tasks.js)
Write a script that computes the number of tasks completed by user id.

```
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping# ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{
  '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12
}
root@69e6d17caa76:/alx-higher_level_programming/0x14-javascript-web_scraping#
```

