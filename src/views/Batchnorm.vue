<template>
    <div class="page">
        <h1>{{title}}</h1>
        <div class="subtitle">
            <img class="author-photo" src="../assets/me.jpg">
            <a href="https://shahparth.net" class="author"><b>Parth Shah</b></a>
            <pre>|  Jan x, 2020  |  x min read</pre>
        </div>
        <div class="body">
            <h3>Prerequisites</h3>
            <small>
                We assume the reader is familiar with the following concepts:
                <ul>
                    <li>Logistic regression or a linear classifier</li>
                </ul>
            </small>
            
            <h2>What is Batch normalization?</h2>
            <p>Batch normalization is a "blah blah".</p>
            <p>
                But, why do we need batchnorm? To understand this we first need to understand a concept called 
                <b>internal covariate shift</b>. If the name sounds intimidating, don't worry, we will break it 
                down into very simple-to-understand pieces.
                
            </p>
            <h2>So, what is internal covariate shift?</h2>
            <p>
                The best way to understand this is to put yourself into the shoes of the model.
            </p>
            <p>
                So, let's play a game. You given dataset of points separated into the yellow and blue classes as shown 
                in the graph below. Your job is to classify them using a linear model. Using the controls for angle
                and y-intercept, adjust the line below to separate the two points. When you are done, press the 
                button below it to see the result.
            </p>
            <Plotly 
                :data="data()" 
                :layout="layout" 
                :display-mode-bar="true"
            ></Plotly>
            <div class="controls">
                <div class="control">
                    <h4 class="control-header">angle</h4>
                    <round-slider
                        v-model="angle"
                        start-angle="0"
                        end-angle="+360"
                        line-cap="round"
                        radius="60"
                        min="0"
                        max="180"
                    />
                </div>
                <div class="control">
                    <h4 class="control-header">intercept</h4>
                    <vue-slider 
                        class="slider"
                        v-model="intercept" 
                        :min="-6"
                        :max="6"
                        :interval=0.1
                        width="300px"
                    />
                </div>
            </div>

            <p>
                Simple enough, right?
            </p>
            
        </div>
        
    </div>
</template>
<script>
import { Plotly } from "vue-plotly"
import BatchnormData from "@/data/batchnorm.json"
import RoundSlider from 'vue-round-slider'
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'

let red = 'rgba(237, 31, 31, 1)'
let green = 'rgba(12, 237, 49, 1)'
let yellow = 'rgba(237, 223, 31, 1)'
let blue = 'rgba(31, 199, 237, 1)'

export default {
    name: "Batchnorm",
    components: {
        Plotly,
        VueSlider,
        RoundSlider
    },
    data(){
        let linspace = []
        for (var i = -100; i<100; i++){
            linspace.push(i/10)
        }
        let data = {
            angle: 45,
            intercept: 0,
            x: linspace,
            title: "Understanding Batch normalization",
            classified: false,
            layout: {
                // title: "My graph",
                autorange: false,
                xaxis:{
                    range: [-10, 10]
                },
                yaxis:{
                    range: [-5, 5]
                },
                showlegend: false,
                colorway:[
                    red,
                    yellow,
                    blue
                ]
            }
        }
        document.title = data.title;
        return data
    },
    methods:{
        line(angle, intercept, x){
            let slope = Math.tan(angle * Math.PI / 180)
            return x.map(p => slope*p + intercept)
        },
        sign(angle, intercept, x, y){
            let slope = Math.tan(angle * Math.PI / 180)
            let anypos = false
            let anyneg = false
            for (let i=0; i<100; i++){
                let s = slope*x[i] + intercept - y[i]
                if (s > 0) anypos = true
                else if (s < 0) anyneg = true
            }
            if(anypos && anyneg){
                return 0
            } else if (anypos) {
                return 1
            } else {
                return -1
            }

        },
        checkClassified(){
            let x1 = BatchnormData["points"]["class1"]["x"]
            let y1 = BatchnormData["points"]["class1"]["y"]
            let x2 = BatchnormData["points"]["class2"]["x"]
            let y2 = BatchnormData["points"]["class2"]["y"]

            let sign1 = this.sign(this.angle, this.intercept, x1, y1)
            let sign2 = this.sign(this.angle, this.intercept, x2, y2)
            if ( sign1 != 0 && sign2 != 0 && sign1 == -1*sign2){
                this.classified = true
                this.layout.colorway[0] = green
            } else {
                this.classified = false
                this.layout.colorway[0] = red
            }
        },
        data(){
            return [
                {
                    x: this.x,
                    y: this.line(this.angle, this.intercept, this.x),
                    type:"scatter"
                },
                {
                    x: BatchnormData["points"]["class1"]["x"],
                    y: BatchnormData["points"]["class1"]["y"],
                    type:"scatter",
                    mode:"markers"
                },
                {
                    x: BatchnormData["points"]["class2"]["x"],
                    y: BatchnormData["points"]["class2"]["y"],
                    type:"scatter",
                    mode:"markers"
                }
            ]
        }
    },
    watch:{
        angle(){
            this.checkClassified()
        },
        intercept(){
            this.checkClassified()
        }
    }
}
</script>
<style lang="scss" scoped>
.page{
    margin: auto;
    padding: 30px;
    width: 100%;
    max-width: 700px;
}
h1{
    font-size: 3rem;
}
.subtitle{
    display: flex;
    padding: 10px;
    align-items: center;
}
$photo-size: 40px;
.author-photo{
    width: $photo-size;
    border-radius: $photo-size / 2;
    margin: 10px;
}
.author{
    margin:10px;
    text-decoration: none;
}
.body{
    text-align: justify;
}
.controls{
    display: flex;
    padding: 10px;
    justify-content: space-evenly;
    align-items: baseline;
    text-align: center;
}
.control{
    margin: 0px 10px;
}
.slider{
    margin-top: 60px;
}
.control-header{
}
</style>
