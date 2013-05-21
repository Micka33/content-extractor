content-extractor
=================

currently, this project parse pdf and psd file to extract meaningful content, such as texts and images both linked into a json string

JSON Format
=================
{
    "pages": [
        {
            "images": [
                "961dfcc0-c1eb-11e2-92af-040ccedc7e34_p0.png"
            ],
            "paragraphs": [
                {
                    "size": 98,
                    "width": 587,
                    "string": "Book Title",
                    "y": -98,
                    "x": -324,
                    "font": "Georgia",
                    "height": 705
                }
            ]
        },
        {
            "images": [
                "96f4e9ee-c1eb-11e2-ad2b-040ccedc7e34_p1.png"
            ],
            "paragraphs": [
                {
                    "size": 24,
                    "width": 138,
                    "string": "CHAPTER 1",
                    "y": -24,
                    "x": -88,
                    "font": "Georgia",
                    "height": 711
                },
                {
                    "size": 33,
                    "width": 489,
                    "string": "Lorem ipsum dolor sit amet, consectetur \n<i>adipisicing</i> <b>elit, sed</b> <i><b>do eiusmod</i></b>\ntempor incididunt ut labore et dolore \nmagna aliqua. Ut enim ad minim veniam,\nquis nostrud exercitation ullamco laboris \nnisi ut aliquip ex ea commodo\nconsequat.",
                    "y": -229,
                    "x": -439,
                    "font": "Georgia",
                    "height": 269
                }
            ]
        },
        {
            "paragraphs": [
                {
                    "size": 24,
                    "width": 133,
                    "string": "SECTION 1",
                    "y": -24,
                    "x": -83,
                    "font": "Georgia",
                    "height": 711
                }
            ]
        }
    ]
}
