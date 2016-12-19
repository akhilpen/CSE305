
fun checker (t1, nil) = false |
checker (t1, t2::ys) = t1=t2
orelse checker (t1, ys);

fun pangram1 (cur, count, str) =
        let
                val ref1 = ref cur
                val refC = ref count
        in
                if !refC < 26 andalso !ref1 > #"z" then "false\n"
                else
                        if !refC = 26 then "true\n"
                        else
                                if checker(!ref1, str) = true then pangram1(chr(ord(!ref1) + 1), !refC + 1, str)
                                else "false\n"
        end;

fun hw1(inputFile : string, outputFile : string) =
let
        val inStream = TextIO.openIn inputFile
        val outStream = TextIO.openOut outputFile
        val readLine = TextIO.inputLine inStream
        fun helper(readLine : string option) =
                case readLine of
                                NONE=>(TextIO.closeIn inStream; TextIO.closeOut outStream)
                                |SOME(a)=>(TextIO.output(outStream, pangram1(#"a", 0, explode(a)));
                                helper(TextIO.inputLine inStream))
in
        helper(readLine)
end

val _ = hw1("input.txt","output.txt")                                         
