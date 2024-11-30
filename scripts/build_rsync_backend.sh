#!/usr/bin/env bash

rm -rf backend
rm reflex-counter-backend.zip
rm reflex_counter_backend.zip
reflex_counter export --backend-only
mkdir backend
cd backend
unzip ../backend.zip
rm -rf scripts
cd ..

zip -r reflex_counter_backend.zip backend
rm -rf backend


rsync -avz reflex_counter_backend.zip root@download.svc.bring.out.ba:/data/download/

