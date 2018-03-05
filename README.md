<h1>Netta-B</h1>
<b>N</b>ot Evil <b>E</b>dit <b>t</b>he <b>T</b>ext <b>A</b>utomatically-functioning <b>B</b>ot

Created by Tikolu. Visit my page on /edit/Tikolu.

<h3>Please note</h3>
I take no responsibility for damage to sites done by this program.
Use for <b>Not Evil</b> purposes only, like backing up or cleaning up pages.
Do not make other people's pages unedittable, <b> especially the main page!</b>

<h2>Installation</h2>
Some computer knowledge required.

<h3>Python</h3>
Download Python 3.6 or newer from <a href="https://www.python.org/downloads/">here</a>.
At the end of the installation select add PYTHON to PATH.

<h3>Requests</h3>
Launch the Windows <a href="https://www.digitalcitizen.life/7-ways-launch-command-prompt-windows-7-windows-8">Command Prompt</a>.
Then, type in <code>pip install requests</code>, and hit enter.

<h3>Netta-B</h3>
Download <a href="https://github.com/Tikolu/nettaB/archive/master.zip">Netta-B</a> and extract the ZIP file.
Now you can create any <code>.py</code> file inside the same folder and it will be able to import Netta-B commands.

<h2>Usage</h2>
Basic Python knowledge required.
At the start of your <code>.py</code> file, write <code>import nettaB</code>.

<h3>Save</h3>
Saves text to a page.
<code>Save(page, text, printOutput)</code>

<code>page</code> - The page you want to edit.

<code>text</code> - What you want the new text on the page to be.

<code>printOutput</code> - Not required, <code>True</code> by default. If True, will print the saved text to the console.

<h5>Examples</h5>
<code>Save("aRandomPage", "This page was editted by Netta-B")</code><br>
Will enter the text <code>This page was editted by Netta-B</code> on the page <code>/edit/aRandomPage</code>.



<h3>Read</h3>
Returns the text of na page.
<code>Read(page)</code>

<code>page</code> - The page you would like to read.

<h5>Examples</h5>
<code>print(Read("aRandomPage"))</code><br>
Will print the contents of the page <code>/edit/aRandomPage</code>.




<h3>IP</h3>
Retruns the IP of the last edittor of a page.
<code>IP(page)</code>

<code>page</code> - The page you would like to get the IP from.

<h5>Examples</h5>
<code>print(IP("aRandomPage"))</code><br>
Will print the IP of the last person that editted <code>/edit/aRandomPage</code>.




<h3>Copy</h3>
Copies the contents of one page to another.
<code>Copy(page, to, printOutput)</code>

<code>page</code> - The page you want to copy from.

<code>to</code> - The page you want to copy to.

<code>printOutput</code> - Not required, <code>True</code> by default. If True, will print the saved text to the console.

<h5>Examples</h5>
<code>Copy("hello","olleh")</code><br>
Will copy all the text from page <code>/edit/hello</code>, to <code>/edit/olleh</code>.

