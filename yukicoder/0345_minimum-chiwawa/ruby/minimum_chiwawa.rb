input = gets
cww_array = []

input.each_char.each_with_index do |char, index|
  if cww_array.length == 0 && char == 'c' then
    cww_array.push(index)
  elsif (cww_array.length == 1 || cww_array.length == 2) && char == 'w' then
    cww_array.push(index)
  end
  if cww_array.length == 3 then
    p(cww_array.last - cww_array.first + 1)
    exit
  end
end

p(-1) if cww_array.length < 3
