<h1 align="center" id="title">Scrcpy Updater</h1>

<p align="center"><img src="https://github.com/Genymobile/scrcpy/raw/master/app/data/icon.svg" alt="project-image"></p>

<p id="description">Using a python script and task scheduler to auto update the Scrcpy.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Reduces the hassle of manually downloading and updating the repo on your machine
*   the script is easy to read so use it for your other favourite repos

<h2>🛠️ Installation Steps:</h2>

<ol>
  <li>
  The default directory where the files will be saved is <i>"C://Tools//Scrcpy"</i>.<br> Remember to change it to your desired directory.
  </li>
  <li>
    Create a new task in the task scheduler: <br>
    <ol>
      <li>
        In the general tab, Enter the task name.<br>&emsp;&emsp;<b>Tick the checkbox for: <i>"Run Whether user is logged in or not"</i> & <i>"Run with highest priviliges"</i></b>
      </li>
      <li>
        In the trigger tab, add a new trigger: <i>On a schedule</i> <br> &emsp;&emsp; Set the timings as per your choice.
      </li>
      <li>
        In the Actions tab, add new action: <b>Start a Program</b> <br> &emsp;&emsp; add <code>python.exe</code> to the <i>Program/Script</i> & add <b> "updater_script_path" </b> to <i>Add arguments</i>
      </li>
      <li>
        In the Conditions tab, tick the checkbox for <i>Start only f following network connection is available</i>. It's to make sure the script doesn't run when there's no internet connectivity.
      </li>
    </ol>
    <li>
      Save the task. Everything's set now so you won't need to auto update the repo.
    </li>
  </li>
</ol>
<h2>Credits:</h2>
<p> All the credits goes toward the awesome developers involved in the development of <a href=https://github.com/Genymobile/scrcpy>Scrcpy</a>. This is just a script i created in my free time.</p>
