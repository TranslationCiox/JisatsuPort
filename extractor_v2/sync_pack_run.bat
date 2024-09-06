@echo off

REM Copy all files from /3.new_files/ subfolders to /0.test_game/modified_files/
for /r "3.new_files" %%f in (*) do (
    copy "%%f" "0.test_game\modified_files\"
)
timeout /t 1 /nobreak
REM Change directory to /0.test_game/
cd 0.test_game/

REM Pack the data and run the executable
j101pack pack Data\data.dat modified_files
timeout /t 1 /nobreak
101.exe
