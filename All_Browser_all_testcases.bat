pytest -v -n=5 --html=HTMLReport/myreport_chrome.html --browser chrome --alluredir="AllureReports" -p no:warnings
pytest -v -n=5 --html=HTMLReport/myreport_firefox.html --browser firefox --alluredir="AllureReports" -p no:warnings
pytest -v -n=5 --html=HTMLReport/myreport_edge.html --browser edge --alluredir="AllureReports" -p no:warnings