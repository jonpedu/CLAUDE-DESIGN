# Vídeo (sem áudio): Canva até 97,5 s + intro a partir de 97,1 s (fade 0,4 s), régua em ilha o vídeo inteiro.
# Quadro 0 = capa (miniatura do WhatsApp). Qualidade máxima: CRF 14, preset slow.
cd "$(dirname "$0")"
H="../../.."
ffmpeg -v error -y -i "$H/video horizontal canva/Hipertensão PET SAUDE - horinzontal.mp4" -i "$H/Intro NTS e PETSAUDE - horizontal.mp4" \
 -loop 1 -i ../camadas/regua_ilha.png -loop 1 -i ../capa_proposta.png \
 -filter_complex "[0:v]trim=0:97.6,setpts=PTS-STARTPTS,fps=30,format=yuv420p[a];[1:v]fps=30,format=yuv420p,setpts=PTS-STARTPTS[b];[a][b]xfade=transition=fade:duration=0.4:offset=97.1[ab];[ab][2:v]overlay=0:0:shortest=1,trim=0:101.7[r];[3:v]format=yuva420p[c];[r][c]overlay=0:0:shortest=1:enable='eq(n,0)',format=yuv420p[v]" \
 -map "[v]" -an -c:v libx264 -preset slow -crf 14 -pix_fmt yuv420p -r 30 final_video.mp4
