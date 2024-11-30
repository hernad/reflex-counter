#!/usr/bin/env bash

rm -rf backend
reflex_counter export --backend-only
mkdir backend
cd backend
unzip ../backend.zip
cd ..
zip -r reflex-counter-backend.zip backend
rm -rf backend

rsync -avz reflex-counter-backend.zip root@download.svc.bring.out.ba:/data/download/

