# Name The Certificate

## :blue_book: Add names in the certificate automatically from excel sheet using Python3.

<hr>

<!-- Installation -->

# :beginner: Installation

### Clone this repository.

```
git clone https://github.com/Alpha-1729/Name_The_Certificate.git
cd Name_The_Certificate
```

## Installing Dependencies

- ### Linux

  You can install all dependencies using the following command in linux terminal.

  ```
  sudo pip3 install -r requirements.txt
  ```

- ### Windows

  You can install all dependencies using the following command in command prompt.

  ```
  pip install -r requirements.txt
  ```

<hr>

# :beginner:Follow These Steps

## Step 1

### Adding certificate image in the image folder.

<ul>
<li>Add the image of the certificate (jpeg or png) in the certificate folder.
<li>Always try to use a jpeg image.
<li>Rename it to certificate.jpg or certificate.png.
</ul>

## Step 2

### Adding the excel file.

<ul>
<li>Add an excel file containing names into the <b>excel</b> folder.
<li>Note the column number of the names in the excel sheet.
<li>Note the range of the row in the excel sheet, that contain the names to be printed.
<li>i.e. <b>starting index</b> and <b>ending index</b>.
</ul>

## Step 3

### Clear the output folder.

<ul>
<li>Remove all images in the <b>output</b> folder.
</ul>

## Step 4

### Adding the font.

<ul>
<li>Download the required <b>true type font</b> from the <a target="_blank" href="https://fonts.google.com/">Google Font.</a>
<li>Add the font file into the <b>font</b> folder.
<li> Sample font is available in the <b>font</b> folder.
</ul>
<hr>

# :beginner:Executing the script.

### Linux

```
python3 main.py
```

### Windows

```
python main.py
```

<hr>

# :beginner:Procedure:

## Step 1

### Selecting the excel, image, font.

<ul>
<li>After executing the script, a dialog box will popup to select excel file, image and font.
<li>Select the excel file containing the names.
<a target="_blank" href="https://raw.githubusercontent.com/Alpha-1729/Name_The_Certificate/master/src/screen_01.png">Click here</a>
<li>Select the image file of the certificate.
<a target="_blank" href="https://raw.githubusercontent.com/Alpha-1729/Name_The_Certificate/master/src/screen_02.png">Click here</a>
<li>Select the font to be used in the certificate.
<a target="_blank" href="https://raw.githubusercontent.com/Alpha-1729/Name_The_Certificate/master/src/screen_03.png">Click here</a>
</ul>

## Step 2

### Fill properties in the terminal.

<ul>
<li> A terminal will be opened asking for some values.
<a target="_blank" href="https://raw.githubusercontent.com/Alpha-1729/Name_The_Certificate/master/src/screen_04.png">Click here</a>
<li>Add the column number containing names in the excel file.
<li>Add the starting index of the row in the excel file.
<li>Add the ending index of the row in the excel file.
<li> Select the style for name in the certificate.
<li>Enter the RGB color code (separate with space) for the name in certificate.
</ul>

## Step 3

### Select the region for name.

<ul>
<li>A screen containing the image will pop out. 
<a target="_blank" href="https://raw.githubusercontent.com/Alpha-1729/Name_The_Certificate/master/src/screen_05.png">Click here</a>
<li>Select the rectangular area where you want to add the name.
<a target="_blank" href="https://raw.githubusercontent.com/Alpha-1729/Name_The_Certificate/master/src/screen_06.png">Click here</a>
<li> After selecting the area, press <b>Enter</b> key.
</ul>

## Step 4

### Adjusting the font size in the certificate.

<ul>
<li>The longest name in the excel file will the shown in the certificate.<a target="_blank" href="https://raw.githubusercontent.com/Alpha-1729/Name_The_Certificate/master/src/screen_07.png">Click here</a>
<li>Press <b>+ key</b> to increase the font-size of the name in the certificate.
<li>Press  <b>- key</b>  to decrease the font-size of the name in the certificate.
<li>After fixing the font, press <b>Enter</b> key.
</ul>

## Step 5

### Selecting the output folder.

<ul>
<li>New dialog box will appear to select the output folder.
<a target="_blank" href="https://raw.githubusercontent.com/Alpha-1729/Name_The_Certificate/master/src/screen_08.png">Click here</a>
<li>Go inside the  folder and select the folder.
<a target="_blank" href="https://raw.githubusercontent.com/Alpha-1729/Name_The_Certificate/master/src/screen_09.png">Click here</a>
<li>After this, all certificates will be created in the <b>output</b> folder.
<a target="_blank" href="https://raw.githubusercontent.com/Alpha-1729/Name_The_Certificate/master/src/screen_10.png">Click here</a>
<br></ul>

<hr>

# :beginner: Note

- If any error happens, kindly report the issue.
- Suggestions are welcome.
