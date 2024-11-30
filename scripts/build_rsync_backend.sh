#!/usr/bin/env bash

rm -rf backend
rm reflex-counter-backend.zip
reflex_counter export --backend-only
mkdir backend
cd backend
unzip ../backend.zip
rm -rf scripts
cd ..

zip -r reflex-counter-backend.zip backend
rm -rf backend


rsync -avz reflex-counter-backend.zip root@download.svc.bring.out.ba:/data/download/

