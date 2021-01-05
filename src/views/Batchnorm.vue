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
            <InteractivePlot></InteractivePlot>
            <p>
                Simple enough, right?
            </p>
            
        </div>
        
    </div>
</template>
<script>
import InteractivePlot from "@/components/InteractivePlot.vue"

export default {
    name: "Batchnorm",
    components: {
        InteractivePlot
    },
    data(){
        return{
            title: "Understanding Batch normalization"
        }
    },
    mounted(){
        document.title = this.title;
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
</style>
