@echo off

git remote remove origin
git remote add origin git@git-iit.fh-joanneum.at:msd-contdel/techdemo-ws24/krall-zarnhofer.git

:: Mirror Repository
git remote set-url --add --push origin git@git-iit.fh-joanneum.at:msd-contdel/techdemo-ws24/krall-zarnhofer.git

:: Main Repository
git remote set-url --add --push origin git@github.com:davkra/krall-zarnhofer.git

git fetch

FOR /F "tokens=*" %%i IN ('git branch --show-current') DO SET CURRENT_BRANCH=%%i
git branch --set-upstream-to=origin/%CURRENT_BRANCH% %CURRENT_BRANCH%

git remote -v
