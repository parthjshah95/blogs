<template>
    <div>
        <Plotly 
            :data="plotData()" 
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
        <div class="button" >Done</div>
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
    name: "InteractivePlot",
    components: {
        Plotly,
        VueSlider,
        RoundSlider
    },
    data(){
        let linspace = []
        for (let i = -10; i<=10; i++){
            linspace.push(i)
        }
        return {
            angle: 45,
            intercept: 0,
            x: linspace,
            classified: false,
            // red: 'rgba(237, 31, 31, 1)',
            // green: 'rgba(12, 237, 49, 1)',
            // yellow: 'rgba(237, 223, 31, 1)',
            // blue: 'rgba(31, 199, 237, 1)',
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
    },
    methods:{
        line(x){
            let slope = Math.tan(this.angle * Math.PI / 180)
            return x.map(p => slope*p + this.intercept)
        },
        sign(x, y){
            let slope = Math.tan(this.angle * Math.PI / 180)
            let anypos = false
            let anyneg = false
            for (let i=0; i<100; i++){
                let s = slope*x[i] + this.intercept - y[i]
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

            let sign1 = this.sign(x1, y1)
            let sign2 = this.sign(x2, y2)
            if ( sign1 != 0 && sign2 != 0 && sign1 == -1*sign2){
                this.classified = true
                this.layout.colorway[0] = green
            } else {
                this.classified = false
                this.layout.colorway[0] = red
            }
        },
        plotData(){
            return [{
                x: this.x,
                y: this.line(this.x),
                // y: [],
                type:"scatter",
                name:"classifier"
            },
            {
                x: BatchnormData["points"]["class1"]["x"],
                y: BatchnormData["points"]["class1"]["y"],
                type:"scatter",
                mode:"markers",
                name:"class 1"
            },
            {
                x: BatchnormData["points"]["class2"]["x"],
                y: BatchnormData["points"]["class2"]["y"],
                type:"scatter",
                mode:"markers",
                name:"class 2"
            }]
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
    // mounted(){
    //     this.plotData[0].y = this.line(this.x)
    // }

}
</script>
<style lang="scss" scoped>
.controls{
    display: flex;
    padding: 0px 10px;
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


