# comfyui-schedulers
测试用scheduler，目前有一个`smooth`调度器

neta lumina下的测试
<p align="center">
    <img src="https://github.com/user-attachments/assets/e23eed4a-58c0-49bd-8444-ab9520a88a9f" width="150" style="margin: 5px;">
    <img src="https://github.com/user-attachments/assets/aace9408-b29e-4962-b5b9-275308f86e58" width="150" style="margin: 5px;">
    <img src="https://github.com/user-attachments/assets/35284db9-93e2-4a13-8660-4b5886e50877" width="150" style="margin: 5px;">
    <img src="https://github.com/user-attachments/assets/39a00d69-bf9e-4bf2-909d-73baa0e5a8f6" width="150" style="margin: 5px;">
</p>

the above schedulers are `normal`,`linear_quadratic`,`sgm_uniform`,`smooth(this repo)`

with neta lumina model in 2048 x 2048（the imgs above are compressed）

prompt:
```
You are an assistant designed to generate anime images based on textual prompts. <Prompt Start>,
draw by @rafaelaaa,@jvn,@nixeu,(liang xing:0.45),(atdan:0.85),(@piromizu:1.1),fov ps,tokkyu,omone hokoma agm,yoneyama mai,void 0,

1girl in a maid dress is smiling towards the viewer.her left eye is purple and her right eye is blue.she has long white hair.


极致的细节, 精彩的光影, 动态光影, 
超高对比度，明暗对比
厚涂3d质感,极致的细节,精彩的光影, 动态光影,极致的景深效果,高对比度,色彩丰富,精细光线,漏光效果,焦外虚化,前景模糊,光线追踪,镜头光晕,电影级打光，超写实背景,光晕，线条清晰,明暗对比,超高清,最高画质,强光,细腻渲染,丰富的细节,高质量,写实逼真,超清晰,


masterpiece, best quality,
```

neg:
```
You are an assistant designed to generate images based on textual prompts. <Prompt Start> ai generated image.blurry, worst quality, low quality
```

step `28`, cfg `4.0`, sampler `euler a`
