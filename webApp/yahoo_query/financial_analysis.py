import yfinance as yf

def financeAnalisis(data):
    rows = []
    info_tags = ['symbol', 'shortName', 'debtToEquity', 'heldPercentInsiders', 'currentPrice', 'targetMeanPrice', 'trailingPE', 'forwardPE', 'trailingEps', 'forwardEps', 'returnOnAssets', 'returnOnEquity', 'profitMargins']
    rows.append(['symbol','shortName','debt/Equ','%Insiders','Price','t.Price','Upside','t.PE','f.PE','t.Eps','f.Eps', 'ROA','ROE','profit.M', 'Myscore', 'Mycount'])
    for i in data:
            data_tags = []
            existant_info_tags = {}
            ticker = yf.Ticker(i)
            count = 0
            for info in info_tags:
                try:
                    existant_info_tags[info] = ticker.info[info]
                except:
                    existant_info_tags[info] = -404
            for key in existant_info_tags:
                    if (key == 'heldPercentInsiders' and existant_info_tags[key] != -404) or (key == 'returnOnAssets' and existant_info_tags[key] != -404) or (key == 'returnOnEquity' and existant_info_tags[key] != -404) or (key == 'profitMargins' and existant_info_tags[key] != -404):
                        data_tags.append(existant_info_tags[key] * 100)
                    elif key == 'debtToEquity' and existant_info_tags[key] != -404:
                        data_tags.append(existant_info_tags[key] / 100)
                    elif key == 'targetMeanPrice' and existant_info_tags[key] != -404:
                        data_tags.append(existant_info_tags[key])
                        data_tags.append(100 * ((existant_info_tags[key] / existant_info_tags['currentPrice']) - 1))
                    elif key == 'targetMeanPrice' and existant_info_tags[key] == -404:
                        data_tags.append(-404)
                        data_tags.append(-404)
                    elif existant_info_tags[key] == -404:
                        data_tags.append(-404)
                    else:
                        data_tags.append(existant_info_tags[key])
            if existant_info_tags['forwardPE'] != -404 and existant_info_tags['trailingPE'] != -404 and existant_info_tags['forwardEps'] != -404 and existant_info_tags['trailingEps'] != -404 and existant_info_tags['debtToEquity'] != -404 and existant_info_tags['heldPercentInsiders'] != -404 and existant_info_tags['targetMeanPrice'] != -404 and existant_info_tags['returnOnEquity'] != -404 and existant_info_tags['profitMargins'] != -404:
                x = 0
                y = 0
                if existant_info_tags['forwardPE'] < existant_info_tags['trailingPE']: 
                    count += 1
                    x = 0.04
                if existant_info_tags['forwardEps'] > existant_info_tags['trailingEps']:
                    count += 1
                    y = 0.03
                data_tags.append(0.08 * 20 * (existant_info_tags['debtToEquity'] / 100) + 0.04 * 2 * existant_info_tags['heldPercentInsiders'] * 100 + 0.35 * 100 * (existant_info_tags['targetMeanPrice'] / existant_info_tags['currentPrice'] - 1) + 0.04 * 2.5 * existant_info_tags['trailingPE'] + x + y + 0.02 * 3.3 * existant_info_tags['returnOnAssets'] * 100 + 0.2 * 0.66 * existant_info_tags['returnOnEquity'] * 100 + 0.2 * 2.5 * existant_info_tags['profitMargins'] * 100)
            else:
                data_tags.append(-404)
            if existant_info_tags['debtToEquity'] < 1 and existant_info_tags['debtToEquity'] != -404:
                count += 1
            if existant_info_tags['heldPercentInsiders'] > 0.05 and existant_info_tags['heldPercentInsiders'] != -404:
                count += 1
            if 100*((existant_info_tags['targetMeanPrice']/existant_info_tags['currentPrice']) - 1) > 50 and existant_info_tags['targetMeanPrice'] != -404 and existant_info_tags['currentPrice'] != -404:
                count += 1
            if existant_info_tags['returnOnAssets'] > 0.15 and existant_info_tags['returnOnAssets'] != -404:
                count += 1
            if existant_info_tags['returnOnEquity'] > 0.2 and existant_info_tags['returnOnEquity'] != -404:
                count += 1
            if existant_info_tags['profitMargins'] > 0.25 and existant_info_tags['profitMargins'] != -404:
                count += 1
            data_tags.append(count)
            rows.append(data_tags)
    return(rows)

def financeAnalisisAl(data):
    rows = []
    try:
        ticker=yf.Ticker(data)
        rows.append([ticker.info['symbol'],ticker.info['shortName'],ticker.info['currentPrice'],ticker.info['targetMeanPrice'],100*((ticker.info['targetMeanPrice']/ticker.info['currentPrice'])-1),ticker.info['trailingPE'],ticker.info['forwardPE'],ticker.info['forwardEps'],ticker.info['debtToEquity'],ticker.info['heldPercentInsiders']*100,ticker.info['ebitdaMargins']*100,ticker.info['operatingMargins']*100,ticker.info['profitMargins']*100,ticker.info['numberOfAnalystOpinions']])
    except:
        pass
        print(IOError)

    return(rows)

if __name__ == "__main__":
    data = ['NA9.DE', 'GOOGL']
    print(financeAnalisis(data))
