import logging
import azure.functions as func

app = func.FunctionApp()

@app.schedule(schedule="* 5 * * * *", arg_name="myTimer", run_on_startup=True,
              use_monitor=False) 
def TestTrigger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('My sample function builds locally!')