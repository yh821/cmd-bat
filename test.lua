------------------------------------------------------------------
------------------------------------------------------------------
------------------------------------------------------------------
------------------------------------------------------------------
------------------------------------------------------------------
------------------------------------------------------------------

local path = "/Users/hugo/Documents/去属性.txt"
local file = io.open(path, "r")
if file then
	local content = file:read("*a")
	print(content)
	io.close(file)
else
	print("文件不存在!", path)
end

------------------------------------------------------------------

-- local bt = 'key1'
-- print(string.sub(bt,1,3))

------------------------------------------------------------------

-- local url = '?account=Oid3Sx4sfRZlgJjltW4V5rqBi3y2&sign=db26c9bc499fb3dcd9a658d467f63463&test=6666&'
-- for m in string.gmatch(url, '[&%?]%w+=%w+') do
-- 	local split = string.find(m, '=')
-- 	local key = string.sub(m, 2, split-1)
-- 	local value = string.sub(m, split+1)
-- 	print(split,key,value)
-- end

------------------------------------------------------------------

-- bit = require 'bit'
-- local encode = function(inpath, outpath, key)
--     local inf = io.open(inpath, 'rb')
--     local outf = io.open(outpath, 'wb')

--     if key == nil or (type(key) ~= 'string') or (string.len(key) == 0) then
--         key = 'md5'
--     end

--     local temp = nil
--     local data = inf:read(1)
--     while data do
--         temp = bit.bxor(string.byte(data), string.byte(string.sub(key, 1, 1)))
--         for i = 2, string.len(key) do
--             temp = bit.bxor(temp, string.byte(string.sub(key, i, i)))
--         end
--         outf:write(string.char(temp))
--         data = inf:read(1)
--     end

--     inf:close()
--     outf:close()
-- end

-- local inpath = '/Users/m5pro/Desktop/test/loadingImage_1.jpg'
-- local outpath = '/Users/m5pro/Desktop/test/loadingImage_2.jpg'
-- local afterpath = '/Users/m5pro/Desktop/test/loadingImage_3.jpg'
-- -- encode(inpath,outpath)
-- encode(outpath,afterpath)

------------------------------------------------------------------

-- local cjson = require 'cjson'
-- local writablePath = '/Users/m5pro/Desktop/test/'
-- local function write_json_file(filename, input)
--     local f = io.open(writablePath .. filename,'w+')
--     f:write(cjson.encode(input))
--     f:close()
-- end
-- local function read_json_file(filename, default)
--     local f = io.open(writablePath .. filename,'r')
--     if f == nil then
--         return default
--     end
--     local content = f:read('*all')
--     f:close()
--     return cjson.decode(content)
-- end

-- local tb = {}--read_json_file('test.json')
-- tb.test = 666
-- tb.array = {1,2,3,0,6}
-- write_json_file('test.json',tb)

------------------------------------------------------------------

--print('hello world!')
--print(string.find('wahahahahhaohaoheheheheh', 'hao'))

--local tt = { 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 }
--print(select(1, tt))
--loginControl = {}
--loginControl.isOpenRegister = not loginControl.isOpenRegister
--print(loginControl.isOpenRegister)

------------------------------------------------------------------

-- print(os.date('%h', 1))
-- print(os.date('%Y-%m-%d %H:%m:%S'))
-- local time = '12:10:00'
-- local year = os.date('%Y')
-- local month = os.date('%m')
-- local day = os.date('%d')
-- print(year,month,day)
-- local dateList = {}
-- for i = 1, 14 do
--     local date = os.time({ year = year, month = month, day = day })
--     dateList[i] = string.format('%s %s', os.date('%Y-%m-%d', date), time)
--     day = day + 1
-- end
-- print(table.concat(dateList, ';\n'))
------------------------------------------------------------------

--a = {}
--a['1'] = 1
--a['2'] = 2
--a['5'] = 3
----print(#a)
--a['4'] = 4
----print(#a)

--for i, v in pairs(a) do
--	print(i, v)
--end

--print(getmetatable('hello world'))
--print(getmetatable(666))

--local x = math.pi
--print(x)
--print(x - x % 0.01)
--print(math.e)

------------------------------------------------------------------

--local tt = {}
--tt.a = 1
--tt.b = 'rmb'
--tt.c = 66

--local tx = { 5, 'he', 66 }

--print(table.concat(tt, ';'))
--print(table.concat(tx, ';'))

------------------------------------------------------------------

--bb = { [0] = '0', [1] = '1', [2] = '2' }
--print(#bb)
--print(bb[0])
--for i, v in ipairs(bb) do
--	print(i, v)
--end

------------------------------------------------------------------

--print(os.date('%Y-%m-%d %H:%M:%S', os.time()))
--print(os.time())

------------------------------------------------------------------

--function encodeURI(s)
--	s = string.gsub(s, '([^%w%.%- ])', function(c)
--		return string.format('%%02X', string.byte(c))
--	end)
--	return string.gsub(s, ' ', '+')
--end

--function decodeURI(s)
--	    s = string.gsub(s, '%%(%x%x)', function (h) return string.char(tonumber(h, 16))
--	end )
--	    return s
--end

--function encodeURI(s)
--	    s = string.gsub(s, '([^%w%.%- ])', function (c) return string.format('%%%02X', string.byte(c))
--	end)
--	    return  string.gsub(s, ' ', '+')
--end

--local url = 'https://game.lzgame.top/index/game/play?bundle_id=com.yjjxwl.ios&payparam={%22sid%22:%2216536%22,%22uid%22:%22594203%22,%22vip%22:%220%22,%22apple%22:%22com.yjzx.30%22,%22goods%22:%22300元宝%22,%22fee%22:%2230%22,%22attach%22:%22role=179323032|device=2|item=3%22}&uid=594203&token=5574ed8d2c29fe7377426ff959e2c4c2&vip=0&currencycode=CN&countrycode=CN&wxjbtoapp=1&getorder=1&pf=3&inm=1&rfapp=1&gameid=55&exmodel=iPhone9,1&version=1.0&sdkver=1.3&sdk=10&out_trade_no=55-84254-1575422511'
--url = string.gsub(url, '{', '%%7B')
--url = string.gsub(url, '}', '%%7D')
--url = string.gsub(url, '|', '%%7C')
--url = string.gsub(url, '元宝', '%%E5%%85%%83%%E5%%AE%%9D')
--print(url)
--local url2 = 'https%3A%2F%2Fgame%2Elzgame%2Etop%2Findex%2Fgame%2Fplay%3Fbundle%5Fid%3Dcom%2Eyjjxwl%2Eios%26payparam%3D%7B%2522sid%2522%3A%252216536%2522%2C%2522uid%2522%3A%2522594203%2522%2C%2522vip%2522%3A%25220%2522%2C%2522apple%2522%3A%2522com%2Eyjzx%2E30%2522%2C%2522goods%2522%3A%2522300%E5%85%83%E5%AE%9D%2522%2C%2522fee%2522%3A%252230%2522%2C%2522attach%2522%3A%2522role%3D179323032%7Cdevice%3D2%7Citem%3D3%2522%7D%26uid%3D594203%26token%3D5574ed8d2c29fe7377426ff959e2c4c2%26vip%3D0%26currencycode%3DCN%26countrycode%3DCN%26wxjbtoapp%3D1%26getorder%3D1%26pf%3D3%26inm%3D1%26rfapp%3D1%26gameid%3D55%26exmodel%3DiPhone9%2C1%26version%3D1%2E0%26sdkver%3D1%2E3%26sdk%3D10%26out%5Ftrade%5Fno%3D55%2D84254%2D1575422511'

--print(lua_util.url_encode(url))

------------------------------------------------------------------

--local date = os.time({ year = 2018, month = 8, day = 17, hour = 0, minute = 0, second = 0 })
--print(date)
--print(tostring(os.time()))

------------------------------------------------------------------

-- function f1(n)
-- 	--函数参数也是局部变量
-- 	local function f2()
-- 		print(n) --引用外包函数的局部变量
-- 	end
-- 	return f2
-- end
-- g1 = f1(100)
-- g1() --打印出100
-- g2 = f1(200)
-- g2() --打印出200
-- g1() --打印出100

-- print('--------------')

-- function f1(n)
-- 	local a = 1
-- 	local function f2()
-- 		print('n:' .. n)
-- 		print('a:' .. a)
-- 	end
-- 	n = n + 10
-- 	a = a + 1
-- 	return f2
-- end

-- g1 = f1(300)
-- g1() --打印出310

------------------------------------------------------------------

-- local jsonstr = '{'kkfix' =>> '1','kk' =>> '(\n{\ntit=\'\\U8d26\\U53f7\\U4e2d\\U5fc3\';\nui=\'aH\'}\n)'}'
-- -- jsonstr = string.gsub(jsonstr, '\\n', '\n')
-- -- jsonstr = string.gsub(jsonstr, '\\\'', '\'')
-- -- jsonstr = string.gsub(jsonstr, '\'{', '{')
-- -- jsonstr = string.gsub(jsonstr, '}\'', '}')
-- jsonstr = string.gsub(jsonstr, '%(.+%)', 'nil')
-- print(jsonstr)

------------------------------------------------------------------

-- local index = string.find('test%sff','%s')
-- print(index)

------------------------------------------------------------------

-- local str = 'abcdefghijklmnopqrstuvwxyz'
-- print(string.sub(str,20,30))

------------------------------------------------------------------

-- local url = 'http://cdn.tramtienquyet.vn/viet_res_ios/publish/iOS/CDN.json'
-- local regex = '/iOS.+CDN.json'
-- print(string.find(url,'httsp'))
-- print(string.sub(url,string.find(url,regex)))

------------------------------------------------------------------
-- math.randomseed(os.time())

-- local items = {
-- 	{'A',200},
-- 	{'B',150},
-- 	{'C',100},
-- 	{'D',50},
-- 	{'E',40},
-- 	{'F',30},
-- 	{'G',20},
-- 	{'H',10},
-- }
-- local all = 0
-- for i,v in ipairs(items) do
-- 	all = all + v[2]
-- end

-- local function getlottery(items,index)
-- 	local sum = 0
-- 	for i,v in ipairs(items) do
-- 		sum = sum + v[2]
-- 		if index<=sum then
-- 			return v[1]
-- 		end
-- 	end
-- end

-- for i=1,1 do
-- 	local index = math.random(all)
-- 	print(getlottery(items,index),index)
-- end

------------------------------------------------------------------

-- local function tableToUrl(data)
-- 	local url = ''
-- 	local first = true
-- 	for k, v in pairs(data) do
-- 		if first then
-- 			first = nil
-- 			url = string.format('%s=%s',k,v)
-- 		else
-- 			url = string.format('%s&%s=%s',url,k,v)
-- 		end
-- 	end
-- 	return url
-- end

-- local function tableToArray(data)
-- 	local array = {}
-- 	for k, v in pairs(data) do
-- 		table.insert(array, k)
-- 		table.insert(array, v)
-- 	end
-- 	return array
-- end

-- local info = {}
-- info.istest = 1
-- info.account = 'userid'
-- info.serverId = 'serverid'
-- info.role = 'roleid'
-- info.item = 'itemid'
-- info.payType = 1
-- info.receipt_data = 'test'

-- --print(tableToUrl(info))
-- local array = tableToArray(info)
-- print(table.concat(array,','))

------------------------------------------------------------------
