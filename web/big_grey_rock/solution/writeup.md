# Big Grey Rectangle writeup

There is a grey rectangle on the website, and nothing more. Let's examine the html:

```html
<body>
    <svg width="40%" viewBox="0 0 1570 100" fill="none" class="center">
        <path d="A LOT OF SYMBOLS SKIPPED" fill="black"/>
    </svg>
    <svg width="90%" height="90%"" class="center">
        <rect width="100%" height="100%" style="fill:#C4C4C4;" />
    </svg> 
</body>
```

Grey rectangle covers some svg. After deleting it, we will see the flag.

P.S. The image is taken from https://wikiway.com/upload/hl-photo/38e/b78/dolina-bekaa_33.jpg

Flag: `li2CTF{H7ML__3d1t3D_5ucc355fully!}`
