import java.io.File

fun readFile(fileName: String): List<String> = File(fileName).readLines()

fun run(){
    val lines = readFile("day14.txt")

    print("done")
    var newLines = mutableListOf<List<String>>()
    var lin = mutableListOf<String>()
    for (l in lines){
        if (l.contains("mask")){
            println(l)
            newLines.add(lin)
            lin.clear()
            lin.add(l)
        }
        else{
            lin.add(l)
        }
    }
    newLines.add(lin)
    println(newLines)
}

run()
