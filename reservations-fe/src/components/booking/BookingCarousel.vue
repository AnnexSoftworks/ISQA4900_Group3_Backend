<template>
    <div class="background-image-container">
        <div
            v-for="(image, index) in images"
            :key="index"
            class="background-image"
            :style="{backgroundImage: `url(${image})`}"
            v-show="currentImageIndex === index">
        </div>
        <div v-if="$slots.title" class="title">
          <slot name="title"></slot>
        </div>
        <div class="content">
            <slot></slot>
        </div>
        <div class="black-mask" :class="maskState"></div>
    </div>
</template>


<script>
import img01 from '../../assets/images/img.png'
import img02 from '../../assets/images/img02.webp'
import img03 from '../../assets/images/img03.webp'
import img04 from '../../assets/images/img04.webp'
import img05 from '../../assets/images/img05.webp'

export default {
    data() {
        return {
            currentImageIndex: 0,
            maskState: '',
            images: [
              img01,
              img02,
              img03,
              img04,
              img05
            ]
        };
    },
    methods: {
        showMask() {
            this.maskState = 'opaque';
            setTimeout(() => {
                this.maskState = 'transparent';
            }, 1000);
        },
        startImageCarousel() {
            setInterval(() => {
                this.showMask();
                setTimeout(() => {
                    this.currentImageIndex++;
                    if (this.currentImageIndex >= this.images.length) {
                        this.currentImageIndex = 0;
                    }
                }, 1000);
            }, 13000);
        }
    },
    mounted() {
        this.startImageCarousel();
    },
    created() {
        this.images.forEach((image) => {
            const img = new Image();
            img.src = image;
        });
    }
};
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css?family=Montserrat:100,200,300,400,500,600,700,800,900');

.background-image-container {
    position: relative;
    width: 100%;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: auto;
}

.content {
    z-index: 10;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 1em;
    box-sizing: border-box;
    width: 100%;
}

.title {
    cursor: default;
    color: white;
    z-index: 10;
    position: absolute;
    top: 80px;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 1em;
    box-sizing: border-box;
    opacity: 70%;
}

.background-image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
}

.black-mask {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
    transition: background-color 1.0s ease-in-out;
}

.black-mask.opaque {
    background-color: rgba(0, 0, 0, 1);
}

.black-mask.transparent {
    background-color: rgba(0, 0, 0, 0.4);
}

@media (max-width: 920px) {
    .title {
        display: none;
    }
}
</style>