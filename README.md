# Project Title: PDF to Audiobook converter

### Description:  
The project uses three libraries namely, pyttsx3 (for text-to-speech), pypdf2 (to read pdf document) and pyAudio (to use the python audio library).  
I installed the three library files using the pip command on the terminal window. PyAudio couldn’t be installed directly onto windows directly, hence I manually installed PyAudio-0.2.11-cp37-cp37m-win32.whl from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio. There is a huge list of versions for PyAudio on the website. Since my system is 32-bit with python 3.7 installed in it, this particular version was compatible with my system.


### Explanation of code:
1.	The pdf to be read, needs to be stored in the same folder as the python file. If not possible, the entire local address of the book must be mentioned within the quotes ‘rb’ indicates reading the file in binary mode. I was initially using ‘r’ mode to read characters as ‘str’ objects, but it gave errors. That is why I used the ‘rb’ mode.  
2.	An object ‘pdfReader’ of the class ‘PyPDF2’ is created. The variable ‘pages’ stores the number of pages in the pdf to help iterating through them in order.  
3.	There are some pre-existing audios made available to use by the module pyttsx3. To use them we can run the following command on hyper after initializing the object ‘speaker’ of the class pyttsx3.  
speaker.getProperty(‘voices’)  
This will give us a list of the available audios along with their voice ids. I personally preferred the female British accent of ‘Hazel’ and hence, I copied her voice id to the variable ‘voice_id’. There are many more audios with options for male/female, accent etc. available for use.  
4.	After this step, I have run a for loop starting at page 7 (where the actual text of the book begins) ang went till the total number of pages in the pdf.  
5.	The ‘page’ variable stores the current page. The ‘text’ variable extracts the text of the pdf from the page. Then the ‘speaker’ object reads out the text using its text-to-speech functionality.  
6.	The voice to be used and the rate at which the narrator speaks can be set to the desired value using the ‘setProperty()’ function of pyttsx3. Then we run the speaker one page at a time.

### Softwares used:  
* Notepad  
* Hyper (terminal)  

[Link to the video of the code](https://youtu.be/JBx5YxrVUF8)
